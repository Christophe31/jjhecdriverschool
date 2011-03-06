<?php

/**
 * insert actions.
 *
 * @package    test
 * @subpackage insert
 * @author     Popi User <popi@popi.local>
 * @version    SVN: $Id: actions.class.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class insertActions extends sfActions {
    /**
     * Executes index action
     *
     * @param sfRequest $request A request object
     */
    public function executeIndex(sfWebRequest $request) {
//   $category = new JjhecCategory();
//   $category->setTitle('Securité');
//   $category->setDescription('La securité c\'est le bien');
//   //$category->save();
//   $category->setDescription('La securité c\'est le bien. Mais compliqué.');
//  //$category->replace();
//
//   $post = new JjhecPost();
//   $post->setAuthorId(1);
//   $post->setCategoryId($category);
//   $post->setTitle('Post 01');
//   $post->setContent('<h1>Le 1er Post</h1>
//       <p>
//       Le 1er post est super mega cool vous trouvez pas ?
//       </p>');
//   //$post->save();
//   for($i=1;$i < 10;$i++){
//        $comment = new JjhecComments();
//        $comment->setAuthorName('popi '.$i);
//        $comment->setContent();
//
// }


    }

    public function executeComments(sfWebRequest $request) {
        //get The Maped Object
        $obj = $request->getRoute()->getObject();
        $this->forward404Unless($cond);
        
        if($request->hasParameter('paramName')){
            $name = $request->getParameter('paramName');
        }
        // Same usage for attrobuts
    }
}
